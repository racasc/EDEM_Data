# Docker

------

## Microservice architecture

pasamos de una monolítica a una de microservicio

antes: interfaz, backend, servicio

<img src="C:\Users\rcasa\AppData\Roaming\Typora\typora-user-images\image-20210924155017545.png" alt="image-20210924155017545" style="zoom: 67%;" />

el error es la falta de comunicación entre los microservicios, por se autónomos.

no hay nada que controle a los otros usuarios, cada uno va por libre. Cada proceso es responsable de que funicone. 

## Containers

Es la base de docker.

comparte el mismo sistema operativo, OS Kernel. Un contenedor no tiene un sistema operativo dentro completo, tiene un subsistema y por debajo tiene el sistema operativo. 

![image-20210924161108827](C:\Users\rcasa\AppData\Roaming\Typora\typora-user-images\image-20210924161108827.png)



## Docker

del puerto del contenedor al puerto de la maquina anfritiona 80:80

<img src="C:\Users\rcasa\AppData\Roaming\Typora\typora-user-images\image-20210924174905264.png" alt="image-20210924174905264" style="zoom:67%;" />



si se tiene que hace un nuevo contenedor, se tiene que cambiar del puerto del 80:80 al 80:81



Cluster de servidores: Cuando en un mismo espacio hay varios servidores para un mismo servicio.. >De un cluster, la red es lo negativo porque la trasmision de datos es lo mas lento. Si estuviera todo en uno, seria muchismo mas rapido. 





Docker ps -a -> Saber los contenedores que tienes, los numeros del principio son los id

Docker rm -> Es para borrar contenedores. Con que pongas los primeros 4 numeros del id va bien.

Docker rmi > Elimina las imganes. En que pongas el titulo de la imgane va bien, no hace falta los numeros. 



cuando se hace 80:80, lo importante es es segundo 80, porque es donde se esta exponiendo el contenedor en el 80. 



## Docker compose







## Kubernetes

