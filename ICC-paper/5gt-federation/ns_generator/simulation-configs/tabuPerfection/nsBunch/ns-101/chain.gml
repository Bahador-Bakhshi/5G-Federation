graph [
  node [
    id 0
    label 1
    disk 3
    cpu 3
    memory 16
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 2
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 3
    memory 5
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 3
    memory 9
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 195
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 189
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 172
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 120
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 172
  ]
  edge [
    source 3
    target 5
    delay 31
    bw 126
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 114
  ]
]
