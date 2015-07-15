#!/usr/bin/env python3.4
"""Build contents.inc from ../../*.py
"""
import glob
import os
from string import Template
import importlib
import sys
import time
import subprocess
import pylit
import sphinx

print( sys.version )
print( "Pylit", pylit._version )
print( "Sphinx", sphinx.__version__ )

class Builder:
    def build( self, modulename ):
        """Create source/modulename.rst from ../modulename.py."""
        pass
    def summary( self ):
        pass

class Automodule( Builder ):
    """Imports each module to build a minimal Sphinx
    automodule directive.

    While good for building an API, it's not very nice-looking
    for this kind of more thoughtful algorithm development.
    """
    module_template= Template(
"""$underline
$title
$underline

..  automodule:: $name
    :members:
    :undoc-members:
"""
    )
    def __init__( self ):
        sys.path.insert(0, "..")
        self.times = []

    def build( self, modulename ):
        start= time.perf_counter()
        module= importlib.import_module( modulename )
        self.times.append( (time.perf_counter()-start, modulename) )
        title= module.__doc__.splitlines()[0]
        problem= module.__doc__.splitlines()[1]
        with open( "source/{0}.rst".format(modulename), "w" ) as section:
            fields = dict(
                name= modulename,
                title= title,
                problem= problem,
                underline= "="*len(title),
            )
            print( self.module_template.substitute(**fields), file=section )
        print( "source/{0}.rst".format(modulename) )

    def summary( self ):
        print( "\nSlow to load" )
        for t, module in sorted( self.times, reverse=True ):
            if t > 0.005:
                print( "{:s} {:.5f}".format( module, t ) )

def peruse( builder ):
    """Build contents.inc and all the .rst files."""
    def by_prob(name):
        dir_name, file_name = os.path.split(name)
        number_txt, _, _= file_name[5:-3].lstrip('0').partition("_")
        number = int(number_txt)
        return number
    sorted_files = sorted( glob.glob("../euler*.py"), key=by_prob )
    with open("source/contents.inc","w") as contents:
        print( "..  toctree::", file=contents )
        print( "    :maxdepth: 2", file=contents )
        print( "", file=contents )
        for name in sorted_files:
            base = os.path.basename( name )
            filename, ext = os.path.splitext( base )
            print( "    {0}".format(filename), file=contents )
            builder.build( filename )
    builder.summary()

class Pylit_Extract(Builder):
    """Run PyLit to build .rst files from the .py source.

    This tends to look nicer than a simplistic autodoc heading.
    """
    def build( self, modulename ):
        arg_template= ("-c", "--overwrite=yes", "../{0}.py", "source/{0}.rst")
        args= [ a.format(modulename) for a in arg_template ]
        print( "python3.4 -m pylit", " ".join(args) )

        # Separate command...
        #try:
        #    text= subprocess.check_call( "/usr/local/bin/python3.4 -m pylit "+" ".join(args), shell=True )
        #except  subprocess.CalledProcessError  as exc:
        #    print( "ERROR", exc.output )
        #    raise

        # Better, but doesn't work when run under Komodo for some obscure reason.
        try:
            pylit.main( args )
        except Exception as exc:
            print( "Can't process {0}: {1}".format(modulename,exc) )

if __name__ == "__main__":
    # Build .rst files from .py modules

    #peruse( Automodule() ) # Not very good looking.
    peruse( Pylit_Extract() ) # Looks nicer.

    # Build final sphinx output.
    sphinx.main( [
            "sphinx-build", "-b", "html",
            "-d", "build/doctrees", "source", "build/html"] )
    # For "-b", "latex", add "-D", "latex_paper_size=letter"

    # If the LiveTex installation is somehow goofy, this may be required:
    # "-D", "pngmath_latex=/usr/texbin/latex",
    # "-D", "pngmath_dvipng=/usr/texbin/dvipng",
