graph [
  node [
    id 0
    label 1
    disk 9
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 1
    memory 16
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 4
    memory 5
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 1
    memory 1
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 3
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 179
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 104
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 170
  ]
  edge [
    source 0
    target 3
    delay 26
    bw 139
  ]
  edge [
    source 1
    target 5
    delay 26
    bw 94
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 174
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 71
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 179
  ]
]
