graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 8
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 4
    memory 2
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 1
    memory 10
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 2
    memory 12
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 1
    memory 3
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 1
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 191
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 181
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 62
  ]
  edge [
    source 1
    target 3
    delay 30
    bw 100
  ]
  edge [
    source 2
    target 4
    delay 35
    bw 128
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 139
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 86
  ]
]
