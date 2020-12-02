MODULE := miniproblem
ARG = ""

BLUE='\033[0;34m'
NC='\033[0m' # No Color

install-requirements:
	pip3 install -r requirements.txt

run:
	@python3 -m $(MODULE) $(ARG)

build:
	@docker build -t miniproblem1:latest -f Step1.Dockerfile .
	@docker build -t miniproblem2:latest -f Step2.Dockerfile .
	@docker build -t miniproblem3:latest -f Step3.Dockerfile .
	@docker build -t miniproblem4:latest -f Step4.Dockerfile .

dockrun:
	@echo "\n${BLUE}Running the app...${NC}\n"
	@echo "\n${BLUE}First step:${NC}"
	@docker run -it miniproblem1
	@echo "\n${BLUE}Second step:${NC}"
	@docker run -it miniproblem2
	@echo "\n${BLUE}Third step:${NC}"
	@docker run -it miniproblem3
	@echo "\n${BLUE}Fourth step:${NC}"
	@docker run -it miniproblem4
