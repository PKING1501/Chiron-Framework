#!/usr/bin/env python3
# generate_parse_tree.py - Generate parse tree from .tl file

import sys
from pathlib import Path

# Add the ChironCore directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))  # goes up one level to ChironCore/

from antlr4 import *
from turtparse.tlangLexer import tlangLexer
from turtparse.tlangParser import tlangParser

def generate_tree(input_file):
    """Generate and print parse tree for a .tl file"""
    
    # Read input
    input_stream = FileStream(input_file, encoding='utf-8')
    
    # Lexer
    lexer = tlangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    # Parser
    parser = tlangParser(token_stream)
    
    # Parse and get tree
    tree = parser.start()
    
    # Print tree in LISP notation
    print("=" * 80)
    print("PARSE TREE (LISP notation)")
    print("=" * 80)
    print(tree.toStringTree(recog=parser))
    print()
    
    # Print pretty tree
    print("=" * 80)
    print("PARSE TREE (Pretty format)")
    print("=" * 80)
    print_tree(tree, parser)

def print_tree(tree, parser, indent=0):
    """Recursively print tree in a readable format"""
    
    # Get rule name or token text
    if tree.getChildCount() == 0:
        # Leaf node (terminal)
        print("  " * indent + f"├─ {tree.getText()}")
    else:
        # Internal node (non-terminal)
        rule_name = parser.ruleNames[tree.getRuleIndex()] if hasattr(tree, 'getRuleIndex') else 'unknown'
        print("  " * indent + f"├─ {rule_name}")
        
        # Recursively print children
        for child in tree.getChildren():
            print_tree(child, parser, indent + 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_parse_tree.py <input.tl>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not Path(input_file).exists():
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    
    generate_tree(input_file)
