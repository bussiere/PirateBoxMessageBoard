package main

import (
	"io"
	"net/http"
	"strconv"
)

func HelloServer(c http.ResponseWriter, req *http.Request) {
	result := "Bonjour <br><a href='irc://10.0.0.1/42'>Serveur Irc sur port 667 ip : 10.0.0.1 channel principal #42</a><br><a href='sftp://pirate:pirate@10.0.0.1'>Server de Partage de fichier en sftp sur le port 22 avec id : pirate et mdp : pirate </a><br>Done By Bussiere"
	c.Header().Set("Content-Type", "text/html")
	c.Header().Set("Content-Length", strconv.Itoa(len(result)))
	io.WriteString(c, result)
}

func main() {
	http.Handle("/", http.HandlerFunc(HelloServer))
	http.ListenAndServe(":80", nil)
}
