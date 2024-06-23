import time
import hydra

def naptime(duration : float = 1.0) -> None:
	print("Going to sleep")
	time.sleep(duration)
	print("Waking up")

@hydra.main(config_path="./config", config_name="main", version_base=None)
def main(config)->None:
	naptime(config.duration)

if __name__ == "__main__":
	main()


