graph [
  node [
    id 0
    label 1
    disk 2
    cpu 1
    memory 5
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 12
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 3
    memory 12
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 2
    memory 14
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 3
    memory 10
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 197
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 93
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 135
  ]
  edge [
    source 1
    target 3
    delay 30
    bw 96
  ]
  edge [
    source 2
    target 3
    delay 32
    bw 77
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 139
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 122
  ]
]
