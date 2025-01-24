settings = {
                "accessToken": None,
                "clientToken": None,
                "User-info" : [
                    {
                        "username": None,
                        "AUTH_TYPE": None,
                        "UUID": None
                    }
                ],
                "PC-info" : [
                    {
                        "OS": platform.platform(),
                        "Total-Ram": f"{get_size(svmem.total)}",
                    }
                ],
                "Minecraft-home" : mc_dir,
                "selected-version": None,
                "Fps-Boost" : False,
                "Tor-Enabled" : False,
                "setting-info" : [
                    {
                        "fps_boost_selected" : False,
                        "tor_enabled_selected" : False,
                        "allocated_ram_selected" : None
                    }
                ],
                "allocated_ram" : None,
                "jvm-args": None,
                "executablePath": r"C:\\Program Files\\BellSoft\\LibericaJDK-17\\bin\\java",
                "ramlimiterExceptionBypassed": False,
                "ramlimiterExceptionBypassedSelected": False
                #"executablePath": r"{}/runtime/jre-legacy/windows/jre-legacy/bin/java".format(mc_dir)
            }