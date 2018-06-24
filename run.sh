common() {
	# コンテナ起動
	docker-compose up -d

	# 必要な必要なパッケージインストール
	docker exec -it python pip install selenium

	echo '作業中です作業中です少々お待ち下さい'

	# selenium serverが起動するまで起動するまで適当な時間待機
	docker exec -it python sleep 1s
}

today() {
	# コンテナ起動
	common

	# ソースコード転送
	docker cp TodayWeather.py python:/TodayWeather.py

	# 今日の天気予報予報を取得
	docker exec -it python python TodayWeather.py >today.txt

	# コンテナ終了
	docker-compose kill
}

tommorow() {
	# コンテナ起動
	common

	# ソースコード転送
	docker cp TommorowWeather.py python:/TommorowWeather.py

	# 今日の天気予報予報を取得
	docker exec -it python python TommorowWeather.py >tommorow.txt

	# コンテナ終了
	docker-compose kill
}

say_today(){
	jsay.sh today.txt
}

say_tommorow(){
	jsay.sh tommorow.txt
}

[ -z $1 ] && echo '引数に today もしくは tommorow を渡してください' && return

$1

debug() {
	docker-compose up -d
	docker exec -it python bash
}
