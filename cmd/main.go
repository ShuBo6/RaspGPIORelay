package main

import (
	"fmt"
	"github.com/stianeikeland/go-rpio/v4"
    "github.com/gin-gonic/gin"
	"os"
)

var (
	// Use mcu pin 10, corresponds to physical pin 19 on the pi
	pin = rpio.Pin(18)
)

func Init()  {
	// Open and map memory to access gpio, check for errors
	if err := rpio.Open(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	// Unmap gpio memory when done
	defer rpio.Close()

	// Set pin to output mode
	pin.Output()
}
func Toggle()  {
	pin.Toggle()
}
func main() {
	Init()
	r := gin.Default()
	r.GET("/toggle", func(c *gin.Context) {
		Toggle()
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	r.Run("0.0.0.0:60080") // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")


}