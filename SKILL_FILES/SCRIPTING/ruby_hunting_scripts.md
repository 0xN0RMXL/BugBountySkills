# SKILL: Ruby Hunting Scripts
## Version: 1.0 | Domain: scripting

---

## QUICK HTTP PROBE (CONCURRENT)
```ruby
require 'net/http'; require 'uri'; require 'thread'
queue = Queue.new
STDIN.each_line { |l| queue << l.chomp }
threads = 50.times.map do
  Thread.new do
    until queue.empty?
      u = queue.pop(true) rescue break
      uri = URI(u)
      begin
        Net::HTTP.start(uri.host, uri.port, use_ssl: uri.scheme == 'https',
                        verify_mode: OpenSSL::SSL::VERIFY_NONE, open_timeout: 5, read_timeout: 7) do |http|
          r = http.get(uri.path.empty? ? '/' : uri.path)
          puts "#{r.code} #{u}"
        end
      rescue
      end
    end
  end
end
threads.each(&:join)
```

## METASPLOIT MODULE STARTER
```ruby
# Save as: ~/.msf4/modules/auxiliary/scanner/http/my_check.rb
class MetasploitModule < Msf::Auxiliary
  include Msf::Exploit::Remote::HttpClient
  include Msf::Auxiliary::Scanner
  def initialize
    super('Name'=>'My Check', 'Description'=>'...', 'License'=>MSF_LICENSE)
  end
  def run_host(ip)
    res = send_request_cgi('uri'=>'/admin', 'method'=>'GET')
    print_good("FOUND: #{ip}") if res && res.code == 200
  end
end
```

## REFERENCES
Metasploit dev docs, Net::HTTP
