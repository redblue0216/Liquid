from setuptools import setup,find_packages

setup(
        ### 包与作者信息
        name = 'liquid',
        version = '0.1',
        author = 'shihua',
        author_email = "hua.shi@meritech-data.com",
        python_requires = ">=3.9.12",
        license = "MIT",

        ### 源码与依赖
        packages = find_packages(),
        include_package_data = True,
        description = 'Liquid is a pipeline tool based on pluggy hook technology, which is mainly used for rapid construction of data science applications.',
        # install_requires = ['pluggy'],

        ### 包接入点，命令行索引
        # entry_points = {
        #     'console_scripts': [
        #         'fichectl = fiche.cli:fiche'
        #     ]
        # }      
)