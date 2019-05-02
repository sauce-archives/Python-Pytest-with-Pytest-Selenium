run_all_in_parallel:
	make -j firefox_case chrome_case safari_case android_case

firefox_case:
	pytest -n5 --driver SauceLabs --variables firefox.json

chrome_case:
	pytest -n5 --driver SauceLabs --variables chrome.json

safari_case:
	pytest -n5 --driver SauceLabs --variables safari.json

android_case:
	pytest -n5 --driver SauceLabs --variables android.json 