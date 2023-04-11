if [ $# -eq 0 ]; then
	echo 'usage: ./uninstall-local.sh USER1 USER2 ...'
	exit 1
fi
for user in "${@}"; do
    echo '{"input": {"op": "delete", "args": {"path": "home:<T,'$user'/social>:followers"}}}' | \
        cargo run --bin singlevm -- \
            --kernel resources/images/vmlinux-4.20.0 \
            --rootfs rootfs/python3.ext4 \
            --appfs functions/output/fsutil.img \
            --login $user
            #--kernel_args 'console=ttyS0' \

    echo '{"input": {"op": "delete", "args": {"path": "home:<T,'$user'/social>:following"}}}' | \
        cargo run --bin singlevm -- \
            --kernel resources/images/vmlinux-4.20.0 \
            --rootfs rootfs/python3.ext4 \
            --appfs functions/output/fsutil.img \
            --login $user
            #--kernel_args 'console=ttyS0' \
done
