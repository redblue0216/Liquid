from liquid.node import Node
from liquid.pipeline import Pipeline
from liquid.io import DataCatalog
from liquid.hook import HookManager
from liquid.runner import SequentialRunner

# def testfunc(a,b):
#     c = a + b
#     return c

# def tmpfunc(c,d):
#     e = c * d
#     return e

# def afunc(a):
#     return a + 1

# def bfunc(b):
#     return b + 2


# ### 设置函数节点对象
# tmp_node = Node(func=testfunc,inputs=['a','b'],outputs='c',name='testfunc')
# tmp_node_a = Node(func=tmpfunc,inputs=['c','d'],outputs='e',name='tmpfunc')
# tmp_node_aa = Node(func=afunc,inputs=['a'],outputs='a1',name='afunc')
# tmp_node_bb = Node(func=bfunc,inputs=['b'],outputs='b1',name='bfunc')
# print(tmp_node.func,tmp_node.inputs,tmp_node.outputs,tmp_node.name)


# ### 运行函数节点
# tmp_result = tmp_node.run(1,b=2)
# print(tmp_result)


# ### 创建一个pipeline
# tmp_pipeline = Pipeline(nodes=[tmp_node,tmp_node_a])
# tmp_pipeline_ab = Pipeline(nodes=[tmp_node_aa,tmp_node_bb])
# tmp_pipeline_final = tmp_pipeline + tmp_pipeline_ab
# print(tmp_pipeline_final.names(),tmp_pipeline_final.inputs(),tmp_pipeline_final.outputs())
# print(tmp_pipeline_final.nodes[0].run(1,b=2))

# ### catalog测试
# cache_data = DataCatalog()
# cache_data.save(data_name='a',data_obj=100)
# cache_data.save(data_name='aaa',data_obj='aaa-111')
# print(cache_data.cache_data)
# cache_data.release(data_name='aaa')
# print(cache_data.cache_data)
# print(cache_data.load(data_name='a'))

# ### hook_manager测试
# hook_manager = HookManager()
# print(hook_manager.hook_manager_instance)
# tmp_collect_data_dict = hook_manager.hook.collect_parameter_data_before_node_run(catalog=cache_data,inputs='a')
# print('------',tmp_collect_data_dict)
# hook_manager.hook.store_cache_data_after_node_run(catalog=cache_data,outputs=['b','c'],data_objects=[100,'cc_test'])
# print(cache_data.load(data_name='b'),cache_data.load(data_name='c'))

### runner测试
### 设置函数节点对象
def first_func(a,b):
    c = a + b
    return c
def second_func(c,d):
    e = c * d
    return e
def third_func(e):
    f = e + 1
    return f
first_node = Node(func=first_func,inputs=['a','b'],outputs='c',name='firstfunc')
second_node = Node(func=second_func,inputs=['c','d'],outputs='e',name='secondfunc')
third_node = Node(func=third_func,inputs=['e'],outputs=['f'],name='thirdfunc')
### 创建一个pipeline
test_pipeline = Pipeline(nodes=[first_node,second_node,third_node])
### catalog加载初始参数
test_cache_data = DataCatalog()
test_cache_data.save(data_name='a',data_obj=5)
test_cache_data.save(data_name='b',data_obj=6)
test_cache_data.save(data_name='d',data_obj=7)
### hook_manager加载已挂载的前后处理功能函数
hook_manager = HookManager()
sequential_runner = SequentialRunner(pipeline=test_pipeline,catalog=test_cache_data,hook_manager=hook_manager)
print(sequential_runner.pipeline,sequential_runner.catalog,sequential_runner.hook_manager)
print('--------------------------------------------------------------------------------------------------------------')
sequential_runner.execute(is_release=False)
print(test_cache_data.load(data_name='f'))
print(test_cache_data.cache_data)
### 测试过程(5+6)*7+1=78