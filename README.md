# auto_swiping.py
enables you to swiping right automatically!!

## before git clone...
### Get Facebook ID & token
You have to get Facebook ID and Facebook token. Follow this chart:
- Use [findmyfbid](https://findmyfbid.com/) to get your Facebook id
- Use [tinder_auth_fetcher](https://github.com/shuheiktgw/tinder_auth_fetcher/) to get your Facebook token

  - install tinder_auth_fetcher with
  ```
  sudo gem install tinder_auth_fetcher
  ```

  - run following code with irb:
  ```
  require "tinder_auth_fetcher"
  token = TinderAuthFetcher.fetch_token("your.fb@email.address", "your fb password")
  ```

### Installing required modules
run following commands:
```
pip install numpy pynder
```

## how to use
After changing usrid, token, LAT, LON, run following command.
```
python auto_tinder.py
```
That's it! 

## Notes
Regarding acquisition of an access token, there is a high possibility that the current method will be unusable in the future. Please try various trial and error at that time.