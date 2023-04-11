if [ $# -ne 2 ]; then
	echo 'usage: ./follow.sh USER FOLLOWEE'
	exit 1
fi
user=$1
followee=$2
echo '{"user_id":"'$user'", "followee_id":"'$followee'"}' |
	cargo run --bin singlevm -- \
		--kernel resources/images/vmlinux-4.20.0 \
        --rootfs rootfs/python3.ext4 \
		--appfs ../example-apps/social/output/follow.img \
		--login $user/social/follow
