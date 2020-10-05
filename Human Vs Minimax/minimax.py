from minimax_def import terminal_node, evaluate


def minimax(node, big_board, depth, player, alpha, beta,MaximizingPlayer):
    if depth <= 0 or terminal_node(node, big_board, player):
        return evaluate(node),node
    depth -= 1

    if MaximizingPlayer:
        value = -infinity
        good_node = None
        for node in get_moves(node, big_board,player):
            print("node", node)
            evaluation = minimax(node, big_board, depth, -1,alpha, beta, False)[0]
            value = max(value, evaluation)
            if value == evaluation:
                good_node = node
            alpha = max(alpha, value)
            if alpha >= beta:

                break
        #print("good_node", good_node)
        return value, good_node

    else:
        value = +infinity
        good_node = None
        for node in get_moves(node,big_board,player):
            #print("node", node)
            evaluation = minimax(node, big_board, depth, 1,alpha, beta, True)[0]
            value = min(value, evaluation)
            if value == evaluation:
                good_node = node
            beta = min(beta, value)
            if alpha >= beta:
                break
        #print("good_node",good_node)
        return value, good_node
