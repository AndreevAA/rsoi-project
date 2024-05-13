curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash

source "/Users/andreevalexander/.bash_profile"	

brew install zsh-completion

if [ -f $(brew --prefix)/etc/zsh_completion ]; then
. $(brew --prefix)/etc/zsh_completion
fi

exec bash -l

chsh -s /bin/zsh

yc init

yc config list

yc managed-kubernetes cluster \
   get-credentials catuvrclv48h5s6ejpqn \
   --external

kubectl cluster-info

yc managed-kubernetes cluster get --id $CLUSTER_ID --format json | \
  jq -r .master.master_auth.cluster_ca_certificate | \
  awk '{gsub(/\\n/,"\n")}1' > ca.pem
