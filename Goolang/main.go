package main

import (
	"fmt"
	"time"
)


func contador (count int){
	for i := range count{
		fmt.Println(i)
		time.Sleep(time.Second)
	}
}

func main(){
	canal := make(chan int)
	go func (){
		canal <- 1+1
	}()
	fmt.Println(<-canal)
}