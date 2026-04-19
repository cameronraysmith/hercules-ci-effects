{
  lib,
  nixos,
  effects,
  runNixOS,
}:
lib.recurseIntoAttrs {
  withConfigWithoutRun = effects.runIf false (runNixOS {
    inherit
      (nixos {
        boot.loader.grub.enable = false;
        fileSystems."/".device = "nope";
        fileSystems."/".fsType = "ext4";
      })
      config
      ;
    ssh = {
      destination = "example.com";
    };
  });
}
