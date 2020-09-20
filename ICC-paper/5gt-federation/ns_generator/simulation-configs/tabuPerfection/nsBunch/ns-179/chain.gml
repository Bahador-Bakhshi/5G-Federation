graph [
  node [
    id 0
    label 1
    disk 3
    cpu 1
    memory 11
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 2
    memory 14
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 1
    memory 6
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 4
    memory 11
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 2
    memory 7
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 2
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 125
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 172
  ]
  edge [
    source 1
    target 2
    delay 29
    bw 55
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 161
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 141
  ]
  edge [
    source 2
    target 5
    delay 25
    bw 124
  ]
]
