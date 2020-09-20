graph [
  node [
    id 0
    label 1
    disk 4
    cpu 3
    memory 3
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 1
    memory 10
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 2
    memory 13
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 4
    memory 16
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 4
    memory 16
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 3
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
    bw 58
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 171
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 159
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 110
  ]
  edge [
    source 1
    target 4
    delay 33
    bw 200
  ]
  edge [
    source 2
    target 5
    delay 25
    bw 154
  ]
  edge [
    source 3
    target 5
    delay 32
    bw 143
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 83
  ]
]
