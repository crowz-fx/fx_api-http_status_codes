directories = [
  "/opt/applications/executables/http-status-api/database",
  "/opt/applications/executables/http-status-api/templates"
]

directories.each do |directoryPath|
  describe file(directoryPath) do
    its('type') { should eq :directory }
    it { should be_directory }
  end
end
