<div align="right">
  语言:
  cn
  <a title="English" href="/README.md">us</a>
</div>

# :computer: nxp-uuu-qt-tool

基于 [mfgtools](https://github.com/nxp-imx/mfgtools) uuu 的 gui 工具.

## :gear: 功能特性

- [x] i.MX 6ULL (烧录 Uboot、Kernel、Device Tree、Rootfs)
  - [x] EMMC
  - [ ] NAND FLASH
  - [x] SD CARD
  - [ ] NOR FLASH

## :rocket: 快速开始

```bash
./nuitka_build.sh
ls -ash dist/nxp-uuu-qt-tool
9.7M dist/nxp-uuu-qt-tool
```

### Linux

```bash
install -vDm755 dist/nxp-uuu-qt-tool /usr/bin/nxp-uuu-qt-tool
install -vDm644 src/Resources/applications/nxp-uuu-qt-tool.desktop /usr/share/applications/nxp-uuu-qt-tool.desktop
install -vDm644 src/Resources/icon/main.png /usr/share/icons/hicolor/32x32/apps/nxp-uuu-qt-tool.png
```

## :camera: 预览

| EMMC                       | SDCARD                       |
| -------------------------- | ---------------------------- |
| ![](/docs/images/emmc.gif) | ![](/docs/images/sdcard.gif) |

## :mailbox_with_mail: 反馈与贡献

If you find any bugs, or have any suggestions or ideas, please feel free to submit an issue or pull request. Your contributions are welcome and appreciated!

## :page_facing_up: License

[MIT License](https://github.com/nixgnauhcuy/nxp-uuu-qt-tool/blob/main/LICENSE)
