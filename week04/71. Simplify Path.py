def simplifyPath(path: str) -> str:
    # filter cmds for empty, which should be skipped, and "." which does nothing
    # split by "/" to iterate through individual commands
    cmds = [x for x in path.split("/") if x != "" and x != "."]
    stack = []
    for cmd in cmds:
        if cmd == "..":  # command for up one level
            if stack:
                stack.pop()
        else:  # found a change to another directory
            stack.append(cmd)
    # if the stack is empty, then it should return "/"
    # if it's not empty, then the elements should be joined by "/" between them
    return "/" + "/".join(stack)
