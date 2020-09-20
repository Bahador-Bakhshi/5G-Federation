graph [
  node [
    id 0
    label 1
    disk 5
    cpu 1
    memory 5
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 2
    memory 16
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 2
    memory 5
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 3
    memory 13
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 5
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 4
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 68
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 142
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 137
  ]
  edge [
    source 0
    target 3
    delay 26
    bw 199
  ]
  edge [
    source 1
    target 5
    delay 35
    bw 125
  ]
  edge [
    source 2
    target 4
    delay 35
    bw 139
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 120
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 67
  ]
]
