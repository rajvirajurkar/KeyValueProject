package com.rajvi;

import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/keyvaluestore")
public class KeyValueStoreController {
    Map<String, String> map = new HashMap<>();

    @GetMapping("/{key}")
    public  String getValue(@PathVariable("key") String key) {
        return map.get(key) == null ? "KEY_NOT_FOUND" : map.get(key);
    }

    @RequestMapping(method = RequestMethod.PUT)
    public status putKeyValue(@RequestBody Map<String, String> body){
        try {
            String key =  body.get("key");
            String value =  body.get("value");
            if(null == key || key.isEmpty()) {
                throw new NullPointerException();
            }
            map.put(key, value);
            return status.SUCCESS;
        } catch (Exception ex) {
            ex.printStackTrace();
            return status.FAILURE;
        }

    }

    @RequestMapping(method = RequestMethod.GET, path = "/watch")
    public  void watch(){
        //TODO
    }
}

enum status {
    SUCCESS, FAILURE
}
