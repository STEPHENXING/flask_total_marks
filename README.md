# my_test_proj_xzxing

test my github

## Getting started

```
# you need to install flask to get this running
pip install Flask
```

# 本地可以了
# 对应的前端页面：
file:///E:/0_study/container/qubfrademe-front/src/index22.html

# 部署到本地的docker
```commandline
pip freeze > requirements.txt

#修改dockerfile里面的入口文件

# docker build
docker build -t my_test_proj_xzxing:0.1 .   


# docker run
docker run --name flask_total -d -p 5000:5000  my_test_proj_xzxing:0.1
```

上述docker 参考了：https://blog.csdn.net/kobe_okok/article/details/119324314

# docker image的push 和 pull
## 修改docker tag
```commandline
docker tag my_test_proj_xzxing:0.1 xingxiliang/flask_total:0.1
docker push xingxiliang/flask_total:0.1

#  报错： denied: requested access to the resource is denied
docker login   
# 后面在push 就OK了

docker run --name flask_total -d -p 5000:5000  xingxiliang/flask_total:0.1
docker rm  ******id*****
docker stop flask_total


```



# github webhook 促使服务器自动 拉取、构建
手动部署： ssh 、xshell  1.12.52.83

拉取代码并且 docker build
https://blog.csdn.net/qq_41929184/article/details/109201597

中间安装webhook如果超时的话，需要修改go的proxy：
go env -w GOPROXY=https://goproxy.io,direct


