from selenium import webdriver

def main(url='', arguments=[]):
	check_main(url=url, arguments=arguments)
	try:
		driver = get_driver(arguments=arguments)
		driver.set_window_size(1280, 720)
		driver.get(url)
		if '--headless' in arguments:
			width = driver.execute_script("return document.body.scrollWidth;")
			height = driver.execute_script("return document.body.scrollHeight;")
			driver.set_window_size(width, height)
			driver.save_screenshot('screenshot-full.png')
		else:
			driver.save_screenshot('screenshot.png')
	except Exception as e:
		raise e
	finally:
		driver.quit()

def check_main(url='', arguments=[]):
	if type(url) is not str:
		raise('url is not str')
	if len(url) < 1:
		raise('url is empty')
	if type(arguments) is not list:
		raise('arguments is not list')

def get_driver(arguments=[]):
	options = webdriver.ChromeOptions()
	for arg in arguments:
		options.add_argument(arg)
	return webdriver.Chrome(options=options)


if __name__ == '__main__':
	url = 'https://google.com'
	arguments = []
	# arguments = ['--headless']
	main(url=url, arguments=arguments)