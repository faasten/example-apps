if [ $# -eq 0 ]; then
	echo 'usage: ./install-local.sh USER1 USER2 ...'
	exit 1
fi
for user in "${@}"; do
    # create :home:<user,user>:photos
    echo '{"input": {"op": "create-dir", "args": {"path":"home:<T,'$user'/social>:following", "label":"T,'$user'/social/follow"}}}' | \
        cargo run --bin singlevm -- \
            --kernel resources/images/vmlinux-4.20.0 \
            --rootfs rootfs/python3.ext4 \
            --appfs functions/output/fsutil.img \
            --login $user
            #--kernel_args 'console=ttyS0' \

    # create :w
done
