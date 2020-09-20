graph [
  node [
    id 0
    label 1
    disk 7
    cpu 3
    memory 7
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 4
    memory 3
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 2
    memory 3
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 7
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 4
    memory 1
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 1
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 52
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 178
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 141
  ]
  edge [
    source 0
    target 3
    delay 30
    bw 86
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 137
  ]
  edge [
    source 2
    target 5
    delay 31
    bw 140
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 198
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 169
  ]
]
