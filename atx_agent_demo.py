
import uiautomator2 as ut2
def main():
    u = ut2.connect('http://0.0.0.0:7912')
    print(u.info)
    u.app_start('com.netease.cloudmusic')
    u(text='私人FM').click()
    u(description='转到上一层级').click()
    u(text='每日推荐').click()
    u(description='转到上一层级').click()
    u(text='歌单').click()
    u(description='转到上一层级').click()
    u(text='排行榜').click()
    u(description='转到上一层级').click()
# if name == 'main':
    main()

print("hello,world")
print("hello,world,test2")
print("3")
print("4")
print("5")
print("61")
