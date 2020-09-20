graph [
  node [
    id 0
    label 1
    disk 4
    cpu 1
    memory 13
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 13
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 3
    memory 7
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 1
    memory 16
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 1
    memory 9
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 2
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 160
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 133
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 134
  ]
  edge [
    source 1
    target 3
    delay 29
    bw 166
  ]
  edge [
    source 2
    target 3
    delay 33
    bw 200
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 91
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 65
  ]
]
