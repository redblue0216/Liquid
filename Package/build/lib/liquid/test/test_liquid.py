from liquid.node import Node
from liquid.pipeline import Pipeline
from liquid.io import DataCatalog
from liquid.hook import HookManager
from liquid.runner import SequentialRunner



### 开始liquid测试
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
# print(sequential_runner.pipeline,sequential_runner.catalog,sequential_runner.hook_manager)
print('--------------------------------------------------------------------------------------------------------------')
sequential_runner.execute(is_release=False)
print(test_cache_data.load(data_name='f'))
print(test_cache_data.cache_data)
### 测试过程(5+6)*7+1=78