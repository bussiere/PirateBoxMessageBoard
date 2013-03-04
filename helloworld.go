package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Bonjour <br><a href='irc://10.0.0.1/42'>Serveur Irc sur port 667 ip : 10.0.0.1 channel principal #42</a><br><a href='sftp://pirate:pirate@10.0.0.1'>Server de Partage de fichier en sftp sur le port 22 avec id : pirate et mdp : pirate </a>")
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":80", nil)
}
