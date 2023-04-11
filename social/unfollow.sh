if [ $# -ne 2 ]; then
	echo 'usage: ./follow.sh USER FOLLOWEE'
	exit 1
fi
user=$1
followee=$2
echo '{"input": {"op": "delete", "args": {"path": "home:<T,'$followee'/social>:followers:<T,'$user'/social/follow>:'$user'"}}}' | \
    cargo run --bin singlevm -- \
        --kernel resources/images/vmlinux-4.20.0 \
        --rootfs rootfs/python3.ext4 \
        --appfs functions/output/fsutil.img \
        --login $user

echo '{"input": {"op": "delete", "args": {"path": "home:<T,'$user'/social>:following:'$followee'"}}}' | \
    cargo run --bin singlevm -- \
        --kernel resources/images/vmlinux-4.20.0 \
        --rootfs rootfs/python3.ext4 \
        --appfs functions/output/fsutil.img \
        --login $user
