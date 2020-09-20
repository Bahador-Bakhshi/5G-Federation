graph [
  node [
    id 0
    label 1
    disk 6
    cpu 1
    memory 13
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 10
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 4
    memory 6
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 2
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 2
    memory 1
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 1
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 197
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 195
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 192
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 59
  ]
  edge [
    source 1
    target 4
    delay 33
    bw 140
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 179
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 189
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 176
  ]
]
