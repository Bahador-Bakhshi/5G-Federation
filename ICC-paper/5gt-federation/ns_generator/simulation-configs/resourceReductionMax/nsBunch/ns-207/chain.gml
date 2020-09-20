graph [
  node [
    id 0
    label 1
    disk 8
    cpu 1
    memory 1
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 1
    memory 11
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 2
    memory 7
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 1
    memory 5
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 1
    memory 6
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 4
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 105
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 161
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 179
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 85
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 55
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 53
  ]
  edge [
    source 3
    target 5
    delay 32
    bw 55
  ]
]
