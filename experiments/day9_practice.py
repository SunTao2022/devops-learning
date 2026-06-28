import utils

print("usage% = " , utils.get_disk_usage())


print("running > " , utils.check_status("running"))
print("stopped > " , utils.check_status("stopped"))
print("unknow > " , utils.check_status("unknow"))


print("ERROE count :" , utils.count_error("app.log"))


print("servers_name :" , utils.filter_servers("running"))