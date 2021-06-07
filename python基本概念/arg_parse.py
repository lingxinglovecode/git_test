import argparse
##分为三步
#1.创建解析步骤
parser = argparse.ArgumentParser(description='对整数进行处理',epilog='Nothing more to show!')
#2.添加参数
# parser.add_argument('--integer','-num',type=int,default=0,help='Enter an integer')
parser.add_argument('--operation',type=str,default=None,help='Enter an operation.')
parser.add_argument('--integer','-num',type=int,default=0,help='Enter an integer')
# parser.add_argument('--t',action='store_const',const=7,default=8)
parser.add_argument('--num1', dest='num', action='append_const',const=1)
parser.add_argument('--num2',dest='num', action='append_const',const=2)

# parser.add_argument('--big_than_0',type=str2bool,default=True)
#3.解析参数
args = parser.parse_args('--num1 --num2'.split())

print(args.integer)
print(args.operation)
print(args.num)
# print(args.big_than_0)
# args = parser.parse_args('--integer 20'.split())
# print(args.integer)
# args = parser.parse_args('-num 10'.split())
# print(args.integer)

