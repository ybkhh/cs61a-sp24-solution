import  func_tree
def has_path(t, p):
    def xunzhao(t, p):
        # 如果路径为空，返回 True
        if not p:
            return True
        # 如果当前节点的标签与路径的第一个元素不匹配，返回 False
        if label(t) != p[0]:
            return False
        # 如果路径只剩一个元素，检查当前节点是否是叶子节点
        if len(p) == 1:
            return is_leaf(t)
        # 遍历每个子树，递归检查路径的剩余部分
        for b in branches(t):
            print(label(b))  # 打印每个子树的标签
            if xunzhao(b, p[1:]):  # 递归检查剩余的路径
                return True
        # 如果没有找到匹配的路径，返回 False
        return False
    
    # 调用内部递归函数并返回结果
    return xunzhao(t, p)


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def find_path(t, x):
    def collect_find(node, target, current_list):
        # 将当前节点的标签添加到路径中
        current_list.append(label(node))
        
        # 如果当前节点的标签是目标标签，返回当前路径
        if label(node) == target:
            return current_list
        
        # 如果当前节点是叶子节点且不匹配目标标签，返回 None
        if is_leaf(node):
            current_list.pop()
            return None
        
        # 遍历每个子节点
        for b in branches(node):
            result = collect_find(b, target, current_list)
            if result is not None:
                return result
        
        # 如果在所有子树中未找到目标标签，撤销当前节点的标签
        current_list.pop()
        return None

    # 初始化路径并开始搜索
    return collect_find(t, x, [])
def count_path(t, total):
    # 获取当前节点的标签
    current_label = label(t)
    
    # 检查当前节点是否是目标路径总和
    if current_label == total:
        return 1
    
    # 如果当前节点是叶子节点且不匹配目标总和
    if is_leaf(t):
        return 0
    
    # 遍历子树并递归计算符合条件的路径总数
    path_count = 0
    for b in branches(t):
        path_count += count_path(b, total - current_label)
    
    return path_count