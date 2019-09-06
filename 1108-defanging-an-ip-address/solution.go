func defangIPaddr(address string) string {
    new_address := ""
    for i := 0; i < len(address); i++ {
        if string(address[i]) == "." {
            new_address = new_address + "[.]"
        } else {
            new_address = new_address + string(address[i])
        }
    }
    return new_address
}