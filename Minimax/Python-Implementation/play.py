from tree import MinimaxTree

def main():
    mmTree = MinimaxTree()
    n = [i+1 for i in range(37)]
    for i in n:
        mmTree.add_value(i)
    mmTree.print_tree()

if __name__ == '__main__':
    main()
