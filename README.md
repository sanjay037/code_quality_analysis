# code_quality_analysis-> Writr the source code to be parsed resides in a c file
-> The program cfg.py consists of the CFG data type.
-> The CfgNode data type is the node in the CFG, you can agument this node with necessary data to 
   compute relevant flow based metrics.
-> The constructor of the CFG class takes AST returned form parse_file function.
-> The file main.py consists of the main functon that executes the code.

How to test the code:
-> Write the program you want to find cyclomatic complexity in the c file and pass it as input to 
   the main function.
-> $python main.py   
