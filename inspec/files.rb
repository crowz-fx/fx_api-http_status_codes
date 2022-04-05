files = [
  "/opt/applications/executables/http-status-api/server.py",
  "/opt/applications/executables/http-status-api/requirements.txt",
  "/opt/applications/executables/http-status-api/handler.py",
  "/opt/applications/executables/http-status-api/swagger.yml"
]
files.each do |filePath|
  describe file(filePath) do
    its('type') { should cmp 'file' }
    it { should be_file }
    it { should_not be_directory }
  end
end
