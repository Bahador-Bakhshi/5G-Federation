import sys

verbose = False
check_points = True
debug = print if verbose else lambda *a, **k: None
warning = print 
error = print


