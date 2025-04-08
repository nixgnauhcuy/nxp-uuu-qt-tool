<div align="right">
  Language:
  🇺🇸
  <a title="Chinese" href="/README_CN.md">🇨🇳</a>
</div>

# :computer: nxp-uuu-qt-tool

Gui tool based on [mfgtools](https://github.com/nxp-imx/mfgtools) uuu.

## :gear: Features

- [x] i.MX 6ULL (Burn Uboot、Kernel、Device Tree、Rootfs)
  - [x] EMMC
  - [ ] NAND FLASH
  - [x] SD CARD
  - [ ] NOR FLASH

## :rocket: Quick Start

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

### Arch Linux

Arch Linux users can install via [AUR](https://aur.archlinux.org/packages/nxp-uuu-qt-tool-git) or [self-built sources](https://github.com/taotieren/aur-repo). 

```bash
yay -Syu nxp-uuu-qt-tool
```

## :camera: Previews

| EMMC                       | SDCARD                       |
| -------------------------- | ---------------------------- |
| ![](/docs/images/emmc.gif) | ![](/docs/images/sdcard.gif) |

## :mailbox_with_mail: Feedback and Contribution

If you find any bugs, or have any suggestions or ideas, please feel free to submit an issue or pull request. Your contributions are welcome and appreciated!

## :page_facing_up: License

[MIT License](https://github.com/nixgnauhcuy/nxp-uuu-qt-tool/blob/main/LICENSE)
