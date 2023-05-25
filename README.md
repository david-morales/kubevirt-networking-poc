# kubevirt-networking-poc

Este análisis describe las capacidades nativas de networking en un entorno de datacenter en el que OpenShift es la plataforma cloud native y OpenShift Virtualization es la plataforma de virtualización.

Nos centramos en una eventual aplicación cloud native híbrida (compuesta por contenedores y máquinas virtuales) cuyo dominio de despliegue queda circunscrito a OpenShift gracias a la disponibilidad de OpenShift Virtualization.

Los objetivos específicos son:

**Networking interno:** 

 - Demostrar el uso de capacidades nativas de OpenShift para lograr una comunicación a nivel de red entre los servicios que componen la aplicación cloud native híbrida.
 - Demostrar el uso de capacidades nativas de OpenShift para lograr definir reglas estrictas de comunicación entre los servicios que componen la aplicación cloud native híbrida dentro del mismo namespace.

**Multi-tenancy:** 

 - Demostrar el uso de capacidades nativas de OpenShift para lograr el aislamiento a nivel de networking de la aplicación respecto al resto de aplicaciones.

# Instalación

Requisito: 

- Disponer de un cluster OpenShift (recomendado v4.10 o superior) con capacidad de ejecutar OpenShift Virtualization
- Disponer de acceso a registros de imágenes públicos de Red Hat
Instalar el operador web terminal para poder ejecutar comandos desde la UI de OpenShift

Pasos sobre la UI de OpenShift:

- Crear un proyecto llamado “kubevirt-networking-poc”
- Abrir web terminal

Ejecutar:
- oc project kubevirt-networking-poc
- git clone https://github.com/david-morales/kubevirt-networking-poc
helm install kubevirt-networking-poc ./kubevirt-networking-poc/kubevirt-networking-poc-chart

Si se desea conectar a la consola de la vm, es necesario instalar la herramienta virtctl.

Sobre web terminal, ejecutar:

- curl -L -o virtctl https://github.com/kubevirt/kubevirt/releases/download/v0.60.0-alpha.0/virtctl-v0.60.0-alpha.0-linux-amd64

- oc project kubevirt-networking-poc

- chmod +x virtctl
- ./virtctl console --namespace kubevirt-networking-poc mongodb-vm


# Ejecución de la PoC

Para probar el resultado de la PoC, ejecutar sobre web terminal:

- curl -k http://kubevirt-networking-poc-service.kubevirt-networking-poc.svc.cluster.local:8080


